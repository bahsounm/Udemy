package com.example.bahsoun.loginexample;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    public void clickFunction(View view){

        EditText username = (EditText) findViewById(R.id.editNameText);

        EditText password = (EditText) findViewById(R.id.editPassText);

        Log.i("Vale", username.getText().toString());
        Log.i("Value", password.getText().toString());

        Toast.makeText(this, "Hi " + username.getText().toString() , Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
