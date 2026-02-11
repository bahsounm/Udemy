package com.example.bahsoun.gridlayout;

import android.media.AudioManager;
import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    MediaPlayer mediaPlayer;

    public void playSound(View view){
        if (mediaPlayer != null) {
            if (mediaPlayer.isPlaying()) {
                mediaPlayer.stop();
            }
            mediaPlayer.release();
            mediaPlayer = null;
        }
        if (view.getId() == R.id.button0){
            mediaPlayer = MediaPlayer.create(this, R.raw.arlong);
        }else if (view.getId() == R.id.button1){
            mediaPlayer = MediaPlayer.create(this, R.raw.bart);
        }else if (view.getId() == R.id.button2){
            mediaPlayer = MediaPlayer.create(this, R.raw.caesar);
        }else if (view.getId() == R.id.button3){
            mediaPlayer = MediaPlayer.create(this, R.raw.hogback);
        }else if (view.getId() == R.id.button4){
            mediaPlayer = MediaPlayer.create(this, R.raw.jinbei);
        }else if (view.getId() == R.id.button5){
            mediaPlayer = MediaPlayer.create(this, R.raw.kanjuro);
        }else if (view.getId() == R.id.button6){
            mediaPlayer = MediaPlayer.create(this, R.raw.luffy);
        }else if (view.getId() == R.id.button7){
            mediaPlayer = MediaPlayer.create(this, R.raw.perona);
        }
        if (mediaPlayer.isPlaying()) {
            mediaPlayer.stop();
        }
        
        if (mediaPlayer != null) {
            mediaPlayer.start();
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
