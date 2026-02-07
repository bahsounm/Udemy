package com.example.bahsoun.higherorlower;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    double randomNumber;

    public void generateRandomNumber(){
        Random rand = new Random();
        randomNumber = rand.nextInt(20)+1;
    }

    public void clickFunction(View view) {
        Log.i("Info", "Button Clicked");

        double number_to_guess = randomNumber;
        EditText usersGuess = findViewById(R.id.userGuess);

        String guessText = usersGuess.getText().toString().trim();

        // Check if empty
        if (guessText.isEmpty()) {
            Toast.makeText(this, "Please enter a guess", Toast.LENGTH_SHORT).show();
            return;
        }

        double users_d_guess;

        // Validate it's a number
        try {
            users_d_guess = Double.parseDouble(guessText);
        } catch (Exception e) {
            Toast.makeText(this, "Please ensure the guess is a number", Toast.LENGTH_SHORT).show();
            return;
        }

        // Compare result
        if (users_d_guess == number_to_guess) {
            Toast.makeText(this, "You Guessed It!", Toast.LENGTH_SHORT).show();
            generateRandomNumber();
        } else if (users_d_guess > number_to_guess) {
            Toast.makeText(this, "Lower", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Higher", Toast.LENGTH_SHORT).show();
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        generateRandomNumber();
    }
}
