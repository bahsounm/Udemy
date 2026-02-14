package com.example.bahsoun.newactivity;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    public void goToNext(View view){
        Intent intent = new Intent(getApplicationContext(), SecondActivity.class);
        Button b = (Button) view;
        intent.putExtra("name", b.getText().toString());

        startActivity(intent);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
