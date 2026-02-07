package com.example.bahsoun.toastdemo;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    public void clickFunction(View view){
        Log.i("Action","Button Clicked");

        ImageView image1 = (ImageView) findViewById(R.id.pic1);
        ImageView image2 = (ImageView) findViewById(R.id.pic2);

        if (image2.getVisibility() == View.VISIBLE){
            image2.setVisibility(View.GONE);
        }else{
            image2.setVisibility(View.VISIBLE);
            }

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
