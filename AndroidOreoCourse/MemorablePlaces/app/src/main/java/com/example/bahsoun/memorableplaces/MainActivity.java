package com.example.bahsoun.memorableplaces;

import android.content.Intent;
import android.location.Address;
import android.location.Geocoder;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    ArrayList<String> titles = new ArrayList<String>();
    ArrayList<String> coords = new ArrayList<String>();
    ArrayAdapter<String> adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView newPlace = (TextView) findViewById(R.id.newPlace);
        ListView placesList = (ListView) findViewById(R.id.placesList);

        adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_2, android.R.id.text1, titles) {
            @Override
            public View getView(int position, View convertView, android.view.ViewGroup parent) {
                View row = super.getView(position, convertView, parent);

                TextView t1 = (TextView) row.findViewById(android.R.id.text1);
                TextView t2 = (TextView) row.findViewById(android.R.id.text2);

                t1.setText(titles.get(position));   // big line
                t2.setText(coords.get(position));   // smaller line under it

                return row;
            }
        };

        placesList.setAdapter(adapter);

        newPlace.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, OpenMap.class);
                startActivityForResult(intent, 1);
            }
        });

        placesList.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Toast.makeText(MainActivity.this, titles.get(position), Toast.LENGTH_SHORT).show();
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == 1 && resultCode == RESULT_OK && data != null) {
            double lat = data.getDoubleExtra("lat", 0);
            double lng = data.getDoubleExtra("lng", 0);

            String coordText = String.format(java.util.Locale.US, "%.5f, %.5f", lat, lng);

            Geocoder geocoder = new Geocoder(getApplicationContext(), Locale.getDefault());
            try{
                List<Address> listAddresses =  geocoder.getFromLocation(lat, lng, 1);

                if(listAddresses != null && listAddresses.size()>0){
                    String address = "";
                    if (listAddresses.get(0).getLocality() != null){
                        address += listAddresses.get(0).getLocality() + " ";
                    }
                    if (listAddresses.get(0).getThoroughfare() != null){
                        address += listAddresses.get(0).getThoroughfare() + ", ";
                    }
                    if (listAddresses.get(0).getAdminArea() != null){
                        address += listAddresses.get(0).getAdminArea() + " ";
                    }
                    if (address.length() > 0) {
                        Log.i("PlaceInfo", address);
                    }else{
                        Log.i("PlaceInfo 2", listAddresses.get(0).toString());
                    }
                    titles.add(address);
                }

            }catch (Exception e){
                e.printStackTrace();
            }
            coords.add(coordText);
            adapter.notifyDataSetChanged();
        }
    }
}