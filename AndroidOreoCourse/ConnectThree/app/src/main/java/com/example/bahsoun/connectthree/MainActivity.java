package com.example.bahsoun.connectthree;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.GridLayout;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    boolean winner_found = false;
    int activePlayer = 0;
    int[] game_state = {2,2,2,2,2,2,2,2,2};
    int [][] winning_Pos = {{0,1,2},{3,4,5},{6,7,8},
                            {0,3,6}, {1,4,7},{2,5,8},
                            {0,4,8},{2,4,6}};

    public void dropIn(View view){
        if (winner_found){
            return;
        }
        ImageView counter = (ImageView) view;

        int tappedCounter = Integer.parseInt(counter.getTag().toString());

        if (game_state[tappedCounter] != 2){
            return;
        }

        game_state[tappedCounter] = activePlayer;

        counter.setTranslationY(-1500);
        if (activePlayer == 0){
            counter.setImageResource(R.drawable.x);
            activePlayer = 1;
        }else{
            counter.setImageResource(R.drawable.o);
            activePlayer = 0;
        }

        counter.animate().translationYBy(1500).setDuration(300);

        for(int[] winningPosition: winning_Pos){
            if (game_state[winningPosition[0]] == game_state[winningPosition[1]] && game_state[winningPosition[1]]== game_state[winningPosition[2]] && game_state[winningPosition[2]] != 2){
                winner_found = true;
                if (activePlayer == 0){
                    Toast.makeText(this,"O has Won", Toast.LENGTH_SHORT).show();
                }else {
                    Toast.makeText(this, "X has Won", Toast.LENGTH_SHORT).show();
                }
            }

        }
    }

    public void clearBoard(View view){
        GridLayout grid = (GridLayout) findViewById(R.id.grid);

        for (int i = 0; i< grid.getChildCount();i++){
            ImageView counter = (ImageView) grid.getChildAt(i);
            counter.setImageDrawable(null);

        }
        winner_found = false;
        activePlayer = 0;
        for (int i = 0; i< game_state.length;i++){
            game_state[i] = 2;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
