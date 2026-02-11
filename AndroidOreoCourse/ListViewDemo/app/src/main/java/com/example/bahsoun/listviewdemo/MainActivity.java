package com.example.bahsoun.listviewdemo;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ListView myListView = (ListView) findViewById(R.id.listView);

        final ArrayList<String> friends = new ArrayList<String>();

        friends.add("Friend 1");
        friends.add("Friend 2");
        friends.add("Friend 3");
        friends.add("Friend 4");
        friends.add("Friend 5");
        friends.add("Friend 6");
        friends.add("Friend 7");
        friends.add("Friend 8");
        friends.add("Friend 9");
        friends.add("Friend 10");
        friends.add("Friend 11");
        friends.add("Friend 12");
        friends.add("Friend 13");
        friends.add("Friend 14");
        friends.add("Friend 15");
        friends.add("Friend 16");
        friends.add("Friend 17");
        friends.add("Friend 18");
        friends.add("Friend 19");
        friends.add("Friend 20");

        ArrayAdapter<String> arrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, friends);

        myListView.setAdapter(arrayAdapter);

        myListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Toast.makeText(getApplicationContext(), "Hello there " + friends.get(i), Toast.LENGTH_SHORT).show();
            }
        });

    }
}
