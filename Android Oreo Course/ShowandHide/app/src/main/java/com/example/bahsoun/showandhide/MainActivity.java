package com.example.bahsoun.showandhide;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    TextView text;

    public void showText(View view){text.setVisibility(View.VISIBLE);}
    public void hideText(View view){text.setVisibility(View.GONE);}


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text = findViewById(R.id.chicken);
    }
}
