package com.example.bahsoun.guesscelebrity;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.MediaPlayer;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity {
    ArrayList<Celebrity> data;
    int currentIndex;
    int correctAnswerIndex;
    ImageView celebImg;
    Button option1;
    Button option2;
    Button option3;
    Button option4;

    public void define_variables() {

        currentIndex = 0;
        correctAnswerIndex = 0;

        celebImg = findViewById(R.id.celebImg);
        celebImg.setVisibility(View.INVISIBLE);

        option1 = findViewById(R.id.option_1);
        option1.setVisibility(View.INVISIBLE);

        option2 = findViewById(R.id.option_2);
        option2.setVisibility(View.INVISIBLE);

        option3 = findViewById(R.id.option_3);
        option3.setVisibility(View.INVISIBLE);

        option4 = findViewById(R.id.option_4);
        option4.setVisibility(View.INVISIBLE);

    }

    public void makeVisible(){
        celebImg.setVisibility(View.VISIBLE);
        option1.setVisibility(View.VISIBLE);
        option2.setVisibility(View.VISIBLE);
        option3.setVisibility(View.VISIBLE);
        option4.setVisibility(View.VISIBLE);
    }

    public class DownloadTask extends AsyncTask<String, Void, String> {

        @Override
        protected String doInBackground(String... urls) {
            StringBuilder result = new StringBuilder();
            HttpURLConnection urlConnection = null;

            try {
                URL url = new URL(urls[0]);
                urlConnection = (HttpURLConnection) url.openConnection();
                urlConnection.setRequestProperty("User-Agent", "Mozilla/5.0");

                InputStream in = urlConnection.getInputStream();
                InputStreamReader reader = new InputStreamReader(in);

                int data = reader.read();
                while (data != -1) {
                    result.append((char) data);
                    data = reader.read();
                }

                return result.toString();

            } catch (Exception e) {
                Log.e("DownloadTask", "Error", e);
                return null;
            } finally {
                if (urlConnection != null) urlConnection.disconnect();
            }
        }

        @Override
        protected void onPostExecute(String result) {
            data = extractWithRegex(result);
            for (Celebrity c : data) {
                Log.i("CELEB_DATA", c.name + " -> " + c.imageUrl);
            }
            showNextCelebrity();
        }

    }

    public class ImageDownloadTask extends AsyncTask<String, Void, Bitmap> {

        @Override
        protected Bitmap doInBackground(String... urls) {
            try {
                URL url = new URL(urls[0]);
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.connect();

                InputStream input = connection.getInputStream();
                Bitmap bitmap = BitmapFactory.decodeStream(input);

                return bitmap;

            } catch (Exception e) {
                e.printStackTrace();
                return null;
            }
        }

        @Override
        protected void onPostExecute(Bitmap bitmap) {
            ImageView celebImg = findViewById(R.id.celebImg);
            celebImg.setImageBitmap(bitmap);
        }
    }

    public static class Celebrity {
        public final String name;
        public final String imageUrl;

        public Celebrity(String name, String imageUrl) {
            this.name = name;
            this.imageUrl = imageUrl;
        }
    }

    public static ArrayList<Celebrity> extractWithRegex(String html) {
        ArrayList<Celebrity> list = new ArrayList<>();

        Pattern p = Pattern.compile(
                "<img[^>]*?src=\"(https://ygo-assets-entities-us\\.yougov\\.net[^\"]+)\"[^>]*?>.*?class=\"entity-name[^\"]*\">(.*?)</span>",
                Pattern.DOTALL
        );

        Matcher m = p.matcher(html);

        while (m.find()) {
            String imageUrl = m.group(1).trim().replace("&amp;", "&");
            imageUrl = imageUrl.replace("pw=70", "pw=300"); // bigger image
            String name = m.group(2).trim();

            list.add(new Celebrity(name, imageUrl));
        }

        return list;
    }

    public void pickAnswer(View view) {

        int selectedIndex = Integer.parseInt(view.getTag().toString());

        if (selectedIndex == correctAnswerIndex) {
            Toast.makeText(this, "Correct", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Wrong", Toast.LENGTH_SHORT).show();
        }

        currentIndex++;
        showNextCelebrity();
    }

    public void showNextCelebrity() {
        if (currentIndex >= data.size()) {
            currentIndex = 0;
        }

        Celebrity current = data.get(currentIndex);

        new ImageDownloadTask().execute(current.imageUrl);

        makeVisible();

        correctAnswerIndex = (int) (Math.random() * 4);

        Button[] buttons = {option1, option2, option3, option4};

        // Track which names we've already used on buttons
        java.util.HashSet<String> usedNames = new java.util.HashSet<>();
        usedNames.add(current.name);

        for (int i = 0; i < 4; i++) {
            if (i == correctAnswerIndex) {
                buttons[i].setText(current.name);
            } else {
                Celebrity randomCeleb;

                // keep picking until we get a name not already used
                do {
                    int randomIndex = (int) (Math.random() * data.size());
                    randomCeleb = data.get(randomIndex);
                } while (usedNames.contains(randomCeleb.name));

                usedNames.add(randomCeleb.name);
                buttons[i].setText(randomCeleb.name);
            }

            buttons[i].setTag(i);
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        define_variables();
        new DownloadTask().execute("https://today.yougov.com/ratings/entertainment/fame/people/all");


    }
}

