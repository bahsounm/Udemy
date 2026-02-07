package com.example.bahsoun.timestable;

import android.media.AudioManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.SeekBar;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SeekBar times_table_for = findViewById(R.id.seekBar);
        times_table_for.setMax(14);
        times_table_for.setProgress(0);

        final ListView myListView = findViewById(R.id.myListView);

        int initialValue = times_table_for.getProgress() + 1;
        ArrayList<Integer> times_table = new ArrayList<>();

        for (int j = 1; j <= 15; j++) {
            times_table.add(j * initialValue);
        }

        ArrayAdapter<Integer> arrayAdapter =
                new ArrayAdapter<>(MainActivity.this,
                        android.R.layout.simple_list_item_1, times_table);

        myListView.setAdapter(arrayAdapter);

        times_table_for.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                int value = i + 1;
                ArrayList<Integer> times_table = new ArrayList<Integer>();
                for (int j = 1; j < 16;j++){
                    times_table.add(j*value);
                }
                ArrayAdapter<Integer> arrayAdapter = new ArrayAdapter<Integer>(getApplicationContext(), android.R.layout.simple_list_item_1, times_table);
                myListView.setAdapter(arrayAdapter);
            }
            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }
            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
    }
}
