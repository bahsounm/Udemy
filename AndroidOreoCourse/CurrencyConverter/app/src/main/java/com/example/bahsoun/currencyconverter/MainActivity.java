package com.example.bahsoun.currencyconverter;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class MainActivity extends AppCompatActivity {
    public void clickFunction(View view){
        Log.i("Action","Button Clicked");

        EditText myTextInput = findViewById(R.id.amount);

        ImageView image1 = (ImageView) findViewById(R.id.pic1);

        double a = Double.parseDouble(myTextInput.getText().toString()) * 1.60;

        String roudnedDollars = String.format("%.2f", a);

        Toast.makeText(this, "CAD: " + roudnedDollars , Toast.LENGTH_SHORT).show();

    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
