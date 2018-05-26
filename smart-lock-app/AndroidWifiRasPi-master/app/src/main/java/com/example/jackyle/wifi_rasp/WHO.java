package com.example.jackyle.wifi_rasp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;

import com.squareup.picasso.Picasso;

public class WHO extends AppCompatActivity {
    public ImageView taswira;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_who);
        taswira = (ImageView) findViewById(R.id.image_product);
        String imageUrl="http://51.38.188.239:3000/";

        Picasso.with(getApplicationContext()).load(imageUrl).into(taswira);
    }
}
