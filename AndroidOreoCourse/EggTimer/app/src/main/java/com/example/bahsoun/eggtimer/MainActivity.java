package com.example.bahsoun.eggtimer;

import android.media.AudioManager;
import android.media.MediaPlayer;
import android.os.CountDownTimer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private SeekBar set_timer;
    private TextView timer;
    private MediaPlayer mediaPlayer;
    private CountDownTimer countDownTimer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        set_timer = (SeekBar) findViewById(R.id.seekBar);
        timer = (TextView) findViewById(R.id.timer);
        Button startButton = (Button) findViewById(R.id.button);

        mediaPlayer = MediaPlayer.create(this, R.raw.perona);

        set_timer.setMax(1800);
        set_timer.setProgress(0);

        set_timer.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                // i is total seconds
                int minutes = i / 60;
                int seconds = i % 60;

                String timer_text = String.format("%02d:%02d", minutes, seconds);
                timer.setText(timer_text);
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) { }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) { }
        });

        // Show "00:00" initially
        timer.setText("00:00");

        // Start countdown when button is pressed
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                // Cancel any existing timer
                if (countDownTimer != null) {
                    countDownTimer.cancel();
                }

                // Get total seconds from SeekBar
                int totalSeconds = set_timer.getProgress();
                if (totalSeconds <= 0) {
                    // nothing to count down
                    return;
                }

                long totalMillis = totalSeconds * 1000L;

                countDownTimer = new CountDownTimer(totalMillis, 1000) {
                    @Override
                    public void onTick(long millisUntilFinished) {
                        int remainingSeconds = (int) (millisUntilFinished / 1000);
                        int minutes = remainingSeconds / 60;
                        int seconds = remainingSeconds % 60;

                        String timer_text = String.format("%02d:%02d", minutes, seconds);
                        timer.setText(timer_text);
                    }

                    @Override
                    public void onFinish() {
                        timer.setText("00:00");
                        mediaPlayer.start();
                    }
                }.start();
            }
        });
    }
}

