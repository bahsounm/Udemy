package com.example.bahsoun.animation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    boolean bart_visible = true;

    public void fade(View view){
        Log.i("Info", "Pic has been clicked");

        ImageView bart = findViewById(R.id.bart);
        ImageView homer = findViewById(R.id.homer);

//        bart.animate().translationXBy(-
//        bart.animate().rotation(180).setDuration(1000);
//        bart.animate().rotation(1800).alpha(0).setDuration(1000);
//        bart.animate().scaleX(0.5f).scaleY(0.5f).setDuration(1000);
        bart.animate().translationXBy(1000);
//        if(bart_visible){
//            bart.animate().alpha(0).setDuration(2000);
//            homer.animate().alpha(1).setDuration(2000);
//            bart_visible= false;
//        }else{
//            bart.animate().alpha(1).setDuration(2000);
//            homer.animate().alpha(0).setDuration(2000);
//            bart_visible= true;
//        }

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ImageView bart = findViewById(R.id.bart);
        bart.setX(-1000);
    }
}
