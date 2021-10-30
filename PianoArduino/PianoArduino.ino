int x;
bool enable;
const int buzz = 3;
#define T_C 262
#define T_CC 278
#define T_D 294
#define T_DC 312
#define T_E 330
#define T_F 349
#define T_FC 370.5
#define T_G 392
#define T_GC 416
#define T_A 440
#define T_AC 466.5
#define T_B 493
#define T_CH 523 

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 pinMode(LED_BUILTIN ,OUTPUT);
}

void loop() {
   while (!Serial.available());
   x = Serial.readString().toInt();
     if (x == 1){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_C);
     }
     else if (x == 2){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_CC);
     }
     else if (x == 3){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_D);
     }
     else if (x == 4){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_DC);
     }
     else if (x == 5){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_E);
     }
     else if (x == 6){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_F);
     }
     else if (x == 7){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_FC);
     }
     else if (x == 8){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_G);
     }
     else if (x == 9){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_GC);
     }
     else if (x == 10){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_A);
     }
     else if (x == 11){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_AC);
     }
     else if (x == 12){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_B);
     }
     else if (x == 13){
      digitalWrite (LED_BUILTIN ,HIGH);
      tone(buzz,T_CH);
     }
     if (x == 0) {
      digitalWrite (LED_BUILTIN ,LOW);
      noTone(buzz);
     }
    
   
}
