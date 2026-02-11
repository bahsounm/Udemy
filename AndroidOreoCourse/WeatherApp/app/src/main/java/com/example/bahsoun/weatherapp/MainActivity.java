package com.example.bahsoun.weatherapp;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {

    public class DownloadTask extends AsyncTask<String, Void, String> {

        @Override
        protected String doInBackground(String... urls){
            String result = "";
            URL url;
            HttpURLConnection urlConnection = null;

            try {
                url = new URL(urls[0]);
                urlConnection = (HttpURLConnection) url.openConnection();
                InputStream in = urlConnection.getInputStream();
                InputStreamReader reader = new InputStreamReader(in);
                int data = reader.read();

                while(data != -1){
                    char current = (char) data;

                    result += current;

                    data = reader.read();
                }
                return result;

            } catch (MalformedURLException e) {
                e.printStackTrace();
                return "Failed";
            } catch (IOException e) {
                e.printStackTrace();
                return "Failed 2";
            }
        }
        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);

            displayResults(result);
        }
    }

    public void onPress(View view){
        Button button = findViewById(R.id.button);

        TextView input = findViewById(R.id.city);

        String city = input.getText().toString();
        if (city.length() <=0){
            Toast.makeText(this, "Must enter a city", Toast.LENGTH_SHORT).show();
        }else{
            new DownloadTask().execute("https://api.openweathermap.org/data/2.5/weather?q= " + city +"&appid=43c4b9279c1ab0faa8184c775137c58b");
        }
    }

    public void displayResults(String result){
        TextView input = findViewById(R.id.city);
        if(result.toUpperCase().contains("failed".toUpperCase())){
            Toast.makeText(this, "Must enter a VALID city", Toast.LENGTH_SHORT).show();
            input.setText("");
        }else {
            try {
                JSONObject jsonObject = new JSONObject(result);

                // City name
                String city = jsonObject.getString("name");

                // Weather array (main + description)
                JSONArray weatherArr = jsonObject.getJSONArray("weather");
                JSONObject weather0 = weatherArr.getJSONObject(0);
                String main = weather0.getString("main");
                String description = weather0.getString("description");

                // Main object (temps etc)
                JSONObject mainObj = jsonObject.getJSONObject("main");
                double tempK = mainObj.getDouble("temp");
                double feelsK = mainObj.getDouble("feels_like");
                int humidity = mainObj.getInt("humidity");

                // Wind
                JSONObject windObj = jsonObject.getJSONObject("wind");
                double windSpeed = windObj.getDouble("speed");

                // Convert Kelvin -> Celsius
                int tempC = (int) Math.round(tempK - 273.15);
                int feelsC = (int) Math.round(feelsK - 273.15);

                TextView results = findViewById(R.id.results);
                results.setText(city + "\n" + main + " - " + description +
                        "\nTemp: " + tempC + "°C (feels " + feelsC + "°C)" +
                        "\nHumidity: " + humidity + "%\nWind: " + windSpeed + " m/s");
                results.setVisibility(View.VISIBLE);
            } catch (Exception e) {
                e.printStackTrace();
            }

        }

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
