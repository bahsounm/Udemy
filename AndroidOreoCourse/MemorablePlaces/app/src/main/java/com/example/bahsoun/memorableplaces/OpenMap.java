package com.example.bahsoun.memorableplaces;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.FragmentActivity;
import android.support.v4.content.ContextCompat;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

public class OpenMap extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private LocationManager locationManager;
    private Marker marker;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);

        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        mMap.setMapType(GoogleMap.MAP_TYPE_HYBRID);

        // Long press: move marker + return result
        mMap.setOnMapLongClickListener(new GoogleMap.OnMapLongClickListener() {
            @Override
            public void onMapLongClick(LatLng latLng) {

                // move/replace marker
                if (marker != null) marker.remove();
                marker = mMap.addMarker(new MarkerOptions().position(latLng).title("Saved place"));
                mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng, 15));

                Intent intent = new Intent();
                intent.putExtra("lat", latLng.latitude);
                intent.putExtra("lng", latLng.longitude);
                setResult(RESULT_OK, intent);
                finish();
            }
        });

        mMap.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(LatLng latLng) {

                // remove old marker
                if (marker != null) marker.remove();

                // title like "43.7001, -79.4163" (rounded)
                String title = String.format(java.util.Locale.US, "%.5f, %.5f",
                        latLng.latitude, latLng.longitude);
                // add new marker
                marker = mMap.addMarker(new MarkerOptions().position(latLng).title(title));
            }
        });

        // Center map on last known location (one-time)
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, 1);
        } else {
            showLastKnownLocation();
        }
    }

    private void showLastKnownLocation() {
        Location last = null;

        // Try GPS first, fallback to network
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)
                == PackageManager.PERMISSION_GRANTED) {
            last = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            if (last == null) {
                last = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
            }
        }

        LatLng start = (last != null)
                ? new LatLng(last.getLatitude(), last.getLongitude())
                : new LatLng(43.6532, -79.3832); // fallback: Toronto

        marker = mMap.addMarker(new MarkerOptions().position(start).title("You"));
        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(start, 12));
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        if (requestCode == 1 && grantResults.length > 0
                && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            showLastKnownLocation();
        }
    }
}