//
// PY371: Electronic Lab for Students
//
// Final Project: Moon Diagram
// Part II: Arduino UNO - C for Arduino
//

const unsigned char PROGMEM img2[] =
{ 
  img2 = Serial.readBytes(256, img2, 256)
};

void drawBitmap(int x, int y, int sx, int sy, unsigned int *data)
{
 int tc = 0;
 for(int Y = 0; Y < sy; Y++)
 {
  for(int X = 0; X < sx; X++)
  {
   display.drawPixel(X+x, Y+y, pgm_read_word(&data[tc]));
   if(tc < (sx*sy)) tc++;
  }
 }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(
}

void loop() {
  // put your main code here, to run repeatedly:
  while (!Serial);
  Serial.println("OK");
  matrix.begin();
  matrix.drawBitmap(0, 0, img2, 256, 256, 0xFFFF);
}
