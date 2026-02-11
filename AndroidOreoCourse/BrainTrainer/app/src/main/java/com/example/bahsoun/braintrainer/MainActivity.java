package com.example.bahsoun.braintrainer;

import android.media.MediaPlayer;
import android.os.CountDownTimer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Random;

public class MainActivity extends AppCompatActivity {

    Button goButton;
    Button option1;
    Button option2;
    Button option3;
    Button option4;

    TextView score;
    TextView timer;
    TextView question;
    TextView correct;
    TextView wrong;

    ImageView clock;

    int leftNumber;
    int rightNumber;
    String op;
    int correctAnswer;

    int questions_right = 0;
    int total_questions = 0;

    MediaPlayer mediaPlayer;

    // Keep references to timers so they don’t multiply out of control
    CountDownTimer gameTimer;
    CountDownTimer feedbackTimer;

    public void define_variables() {
        mediaPlayer = MediaPlayer.create(this, R.raw.theme);

        goButton = findViewById(R.id.goButton);

        option1 = findViewById(R.id.option1);
        option2 = findViewById(R.id.option2);
        option3 = findViewById(R.id.option3);
        option4 = findViewById(R.id.option4);

        score = findViewById(R.id.scoreText);
        timer = findViewById(R.id.timer);
        question = findViewById(R.id.question);
        correct = findViewById(R.id.correct);
        wrong = findViewById(R.id.wrong);

        clock = findViewById(R.id.clock);
    }

    public void clickGo(View view) {
        goButton.setVisibility(View.GONE);

        // Reset score for a new game
        questions_right = 0;
        total_questions = 0;
        score.setText("0/0");

        mediaPlayer.start();

        option1.setVisibility(View.VISIBLE);
        option2.setVisibility(View.VISIBLE);
        option3.setVisibility(View.VISIBLE);
        option4.setVisibility(View.VISIBLE);

        score.setVisibility(View.VISIBLE);
        timer.setVisibility(View.VISIBLE);
        question.setVisibility(View.VISIBLE);
        clock.setVisibility(View.VISIBLE);

        startTimer();
        generateNewQuestion();
    }

    public void startTimer() {
        // Cancel previous timer if somehow still running
        if (gameTimer != null) {
            gameTimer.cancel();
        }

        gameTimer = new CountDownTimer(31000, 1000) {
            @Override
            public void onTick(long millisUntilFinished) {
                int remainingSeconds = (int) (millisUntilFinished / 1000);
                timer.setText(remainingSeconds + "s");
            }

            @Override
            public void onFinish() {
                timer.setText("0s");
                if (mediaPlayer != null) {
                    try {
                        mediaPlayer.stop();
                    } catch (IllegalStateException e) {
                        // ignore if already stopped
                    }
                }

                // Optional: disable buttons when time is up
                option1.setEnabled(false);
                option2.setEnabled(false);
                option3.setEnabled(false);
                option4.setEnabled(false);
            }
        }.start();
    }

    public void generateNewQuestion() {
        Random rand = new Random();

        leftNumber = rand.nextInt(50) + 1;
        rightNumber = rand.nextInt(50) + 1;

        String[] ops = {"+", "-"};
        op = ops[rand.nextInt(ops.length)];

        String problem = leftNumber + " " + op + " " + rightNumber;
        question.setText(problem);

        if (op.equals("+")) {
            correctAnswer = leftNumber + rightNumber;
        } else {
            correctAnswer = leftNumber - rightNumber;
        }

        int correctPosition = rand.nextInt(4);

        ArrayList<Integer> answers = new ArrayList<>();

        for (int i = 0; i < 4; i++) {
            if (i == correctPosition) {
                answers.add(correctAnswer);
            } else {
                int wrong;
                do {
                    wrong = correctAnswer + rand.nextInt(21) - 10; // ±10 range
                } while (wrong == correctAnswer || wrong < 0);

                answers.add(wrong);
            }
        }

        option1.setText(String.valueOf(answers.get(0)));
        option2.setText(String.valueOf(answers.get(1)));
        option3.setText(String.valueOf(answers.get(2)));
        option4.setText(String.valueOf(answers.get(3)));

        // Re-enable buttons in case they were disabled on game over
        option1.setEnabled(true);
        option2.setEnabled(true);
        option3.setEnabled(true);
        option4.setEnabled(true);
    }

    public void display(final String result) {

        // Stop previous feedback timer if user somehow taps again fast
        if (feedbackTimer != null) {
            feedbackTimer.cancel();
        }

        // Update score ONCE per answer, before timer starts
        total_questions++;
        if ("correct".equals(result)) {
            questions_right++;
        }
        score.setText(questions_right + "/" + total_questions);

        feedbackTimer = new CountDownTimer(500, 500) {
            @Override
            public void onTick(long millisUntilFinished) {
                if ("correct".equals(result)) {
                    correct.setVisibility(View.VISIBLE);
                    wrong.setVisibility(View.INVISIBLE);
                } else {
                    wrong.setVisibility(View.VISIBLE);
                    correct.setVisibility(View.INVISIBLE);
                }
            }

            @Override
            public void onFinish() {
                correct.setVisibility(View.INVISIBLE);
                wrong.setVisibility(View.INVISIBLE);
                generateNewQuestion();
            }
        }.start();
    }

    public void checkAnswer(View view) {
        // If game is over (timer at 0), ignore taps
        if ("0s".contentEquals(timer.getText())) {
            return;
        }

        Button clicked = (Button) view;
        String text = clicked.getText().toString();

        // Guard against any weird non-number text
        int chosen;
        try {
            chosen = Integer.valueOf(text);
        } catch (NumberFormatException e) {
            return;
        }

        if (correctAnswer == chosen) {
            display("correct");
        } else {
            display("wrong");
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        define_variables();
    }
}
