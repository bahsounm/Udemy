package com.example.bahsoun.hikerwatch;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    LocationManager locationManager;
    LocationListener locationListener;

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            if(ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
                locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationListener);
            }
        }
    }

    public void onPress(View view){
        final TextView lat = findViewById(R.id.lat);
        final TextView lng = findViewById(R.id.lng);
        final TextView acc = findViewById(R.id.acc);
        final TextView alt = findViewById(R.id.alt);
        final TextView add = findViewById(R.id.add);

        Button getLoc = findViewById(R.id.getLoc);

        locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);

        locationListener = new LocationListener() {
            @Override
            public void onLocationChanged(Location location) {
                Log.i("Location", location.toString());
                locationManager.removeUpdates(this);

                lat.setText("Latitude: " + String.format("%.2f", location.getLatitude()));
                lng.setText("Longitude: " + String.format("%.2f", location.getLongitude()));
                acc.setText("Accuracy: " + String.format("%.2f", location.getAccuracy()));
                alt.setText("Altitude: " + String.format("%.2f", location.getAltitude()));

                String addressString = "Address not found";

                try {
                    Geocoder geocoder = new Geocoder(MainActivity.this, Locale.getDefault());
                    List<Address> list = geocoder.getFromLocation(location.getLatitude(), location.getLongitude(), 1);

                    if (list != null && !list.isEmpty()) {
                        Address a = list.get(0);

                        StringBuilder sb = new StringBuilder();

                        if (a.getSubThoroughfare() != null) sb.append(a.getSubThoroughfare()).append(" ");
                        if (a.getThoroughfare() != null) sb.append(a.getThoroughfare()).append("\n   ");
                        if (a.getLocality() != null) sb.append(a.getLocality()).append("\n   ");
                        if (a.getAdminArea() != null) sb.append(a.getAdminArea()).append("\n   ");
                        if (a.getPostalCode() != null) sb.append(a.getPostalCode()).append("\n   ");
                        if (a.getCountryName() != null) sb.append(a.getCountryName());

                        addressString = sb.toString().trim();
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }

                add.setText("Address: \n   " + addressString);
            }

            @Override
            public void onStatusChanged(String s, int i, Bundle bundle) {

            }

            @Override
            public void onProviderEnabled(String s) {

            }

            @Override
            public void onProviderDisabled(String s) {

            }
        };

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, 1);
        } else {
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationListener);
        }

        return;


    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
