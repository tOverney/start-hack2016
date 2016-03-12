package ch.epfl.all.carousel;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

import java.io.IOException;
import java.io.InputStream;
import java.util.UUID;

import ch.uepaa.p2pkit.P2PKitClient;
import ch.uepaa.p2pkit.P2PKitStatusCallback;
import ch.uepaa.p2pkit.StatusResult;
import ch.uepaa.p2pkit.StatusResultHandling;
import ch.uepaa.p2pkit.discovery.InfoTooLongException;
import ch.uepaa.p2pkit.discovery.P2PListener;
import ch.uepaa.p2pkit.discovery.entity.Peer;
import ch.uepaa.p2pkit.internal.messaging.MessageTooLargeException;
import ch.uepaa.p2pkit.messaging.MessageListener;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getCanonicalName();
    private ImageView imgView;

    private final P2PKitStatusCallback mStatusCallback = new P2PKitStatusCallback() {
        @Override
        public void onEnabled() {
            // ready to start discovery
            Log.d(TAG, "On Enabled");
        }

        @Override
        public void onSuspended() {
            // p2pkit is now suspended
            Log.d(TAG, "On Suspended");
        }

        @Override
        public void onError(StatusResult statusResult) {
            // enabling failed, handle statusResult
            Log.d(TAG, "On error");
        }
    };

    private Peer other;

    private final MessageListener mMessageListener = new MessageListener() {
        @Override
        public void onMessageStateChanged(int state) {
            Log.d(TAG, "MessageListener | State changed: " + state);
            if(other != null) {
                try {
                    InputStream is = getResources().openRawResource(R.raw.duke);
                    int size = is.available();
                    byte[] buffer = new byte[size];
                    is.read(buffer); //read file
                    is.close(); //close file
                    P2PKitClient.getInstance(getApplicationContext()).getMessageServices().sendMessage(other.getNodeId(), "image/jpeg", buffer);
                } catch (MessageTooLargeException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        @Override
        public void onMessageReceived(long timestamp, UUID origin, String type, byte[] message) {
            Log.d(TAG, "MessageListener | Message received: From=" + origin + " type=" + type + " message=" + new String(message));
            Bitmap bmp = BitmapFactory.decodeByteArray(message, 0, message.length);
            ImageView image = (ImageView) findViewById(R.id.imageView1);

            image.setImageBitmap(bmp);
        }
    };
    private final P2PListener mP2PDiscoveryListener = new P2PListener() {
        @Override
        public void onP2PStateChanged(final int state) {
            Log.d(TAG, "P2PListener | State changed: " + state);
        }

        @Override
        public void onPeerDiscovered(final Peer peer) {
            Log.d(TAG, peer.toString());

            other = peer;
            Log.d(TAG, "P2PListener | Peer discovered: " + peer.getNodeId());
            if (peer.getDiscoveryInfo() != null) {
                Log.d(TAG, " with info: " + new String(peer.getDiscoveryInfo()));
            }

        }

        @Override
        public void onPeerLost(final Peer peer) {
            Log.d(TAG, "P2PListener | Peer lost: " + peer.getNodeId());
        }

        @Override
        public void onPeerUpdatedDiscoveryInfo(Peer peer) {
            Log.d(TAG, "P2PListener | Peer updated: " + peer.getNodeId() + " with new info: " + new String(peer.getDiscoveryInfo()));
        }
    };

    private void enableKit() {
        final StatusResult result = P2PKitClient.isP2PServicesAvailable(this);
        if (result.getStatusCode() == StatusResult.SUCCESS) {
            P2PKitClient client = P2PKitClient.getInstance(this);
            client.enableP2PKit(mStatusCallback,
                    "eyJzaWduYXR1cmUiOiJ5UkxjY3ZCc1pEZ2lDMFVINmpIUDN6U1Y4MmVBWEJnVG5GVFJQNGhDTjlYaWJWcko3ckZ4SGFWOGVnemNVWW1oN2dsT21tTFRTUEdxUC9CUitMV0piVHpVMVAwYTNDMzlYTi9JYlV6RUUyM2wrbkpzTTFJZ0UzVS9jNk40R05LRkpTQ3UwZWZLejl2YUVqWVIrM2xRUWxmYzkrSDJtRnpQTG0rNXRHdkRKQzQ9IiwiYXBwSWQiOjE0ODAsInZhbGlkVW50aWwiOjE2OTYyLCJhcHBVVVVJRCI6IjBCREVFODQ4LTUwMDUtNDRCNC1CMEQ4LUNGNkM3MTg4OTI4NCJ9");
            P2PKitClient.getInstance(this).getDiscoveryServices().addP2pListener(mP2PDiscoveryListener);
            P2PKitClient.getInstance(this).getMessageServices().addMessageListener(mMessageListener);
        } else {
            StatusResultHandling.showAlertDialogForStatusError(this, result);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });

        enableKit();

        try {

            P2PKitClient.getInstance(this).getDiscoveryServices().setP2pDiscoveryInfo("Hello".getBytes());
        } catch (InfoTooLongException e) {
            e.printStackTrace();
        }
    }
}
