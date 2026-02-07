package com.example.bahsoun.timerdemo;

import android.os.CountDownTimer;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        new CountDownTimer(10000, 1000){
            public void onTick(long mili_until_done){
                Log.i("Info", "Sec Left" + String.valueOf(mili_until_done/1000));
            }

            public void onFinish(){
                Log.i("Info", "Done");
            }
        }.start();

        // Way 1 of doing a timer
//        final Handler handler = new Handler();
//
//        Runnable run = new Runnable() {
//            @Override
//            public void run() {
//                Log.i("Info", "1 second has passed");
//                handler.postDelayed(this, 1000);
//            }
//        };
//        handler.post(run);
    }
}
