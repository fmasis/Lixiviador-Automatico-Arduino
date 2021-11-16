#include <Servo.h>
#define ENABLE 4
#define DIRB 5
#define DIRA 6
Servo servoMotor;

const int Trigger = 3;   //Pin digital 2 para el Trigger del sensor
const int Echo = 2;   //Pin digital 3 para el Echo del sensor
long d; //distancia en centimetros
bool cond;
int vel = 360;
int startVar = 0;
int mssg;
int tiempos[16];
int cantidades[16];
int tiempo;
int cantidad;
int det;
long t; //timepo que demora en llegar el eco

void setup() {
  Serial.begin(9600);//iniciailzamos la comunicación
  pinMode(Trigger, OUTPUT); //pin como salida
  pinMode(Echo, INPUT);  //pin como entrada
  digitalWrite(Trigger, LOW);//Inicializamos el pin con 0
  pinMode(ENABLE, OUTPUT);
  pinMode(DIRA,OUTPUT);
  pinMode(DIRB,OUTPUT);
  digitalWrite(ENABLE,HIGH);
  digitalWrite(DIRA,HIGH);
  digitalWrite(DIRB,HIGH);
  

  servoMotor.attach(9);
}

void loop()
{
  start();
  //condition();
  //stp();
}

void stp(){
  if(d <= 10){
    Serial.print("MoverMotor");
    delay(10000);
  }
}

void printCant(){
  for(int i = 0; i<=3; i++){
    Serial.println(cantidades[i]);
  }
}

void start(){
  mssg = Serial.parseInt();
  if(mssg != 0){
    //Serial.println(mssg);
    getInterval(mssg);
  }
}

void getInterval(int quant){
  Serial.println(quant);
  for(int i = 0; i <= quant - 1; i++){
    tiempo = Serial.parseInt();
    tiempos[i] = tiempo;
    Serial.println(tiempos[i]);
    cantidad = Serial.parseInt();
    cantidades[i] = cantidad;
    Serial.println(cantidades[i]);
  }
  StartApp(quant);
}

void StartApp(int quant){
  for(int i = 0; i <= quant - 1; i++){
    Serial.println("El valor de i es:");
    Serial.println(i);
    Serial.println("El valor de quant es:");
    Serial.println(quant);
    startInterval(tiempos[i], cantidades[i]);
  }
}

void startInterval(int tiempo, int cantidad){
  Serial.println("Moviendo motor");
  digitalWrite(DIRB, LOW);
  d= 50;
  while(d < 200){
    digitalWrite(Trigger, HIGH);
    delayMicroseconds(10);          //Enviamos un pulso de 10us
    digitalWrite(Trigger, LOW);
    t = pulseIn(Echo, HIGH); //obtenemos el ancho del pulso
    d = microsecondsToMillimeters(t);                        //escalamos el tiempo a una distancia en cm
    //Serial.println(d);
    //Serial.println("cm");
  }Serial.println(d);
  while(d >= 130 || d<=100){
    digitalWrite(Trigger, HIGH);
    delayMicroseconds(10);           //Enviamos un pulso de 10us
    digitalWrite(Trigger, LOW);
    t = pulseIn(Echo, HIGH);         //obtenemos el ancho del pulso
    d = microsecondsToMillimeters(t);//escalamos el tiempo a una distancia en cm
    //Serial.println(d);
    //Serial.println("cm");
  }
  Serial.println("Deteniendo motor");
  digitalWrite(DIRB, HIGH);
  digitalWrite(DIRA, LOW);
  delay(95);
  digitalWrite(DIRA, HIGH);
  Serial.println(d);
  Serial.println("El tiempo de espera es de:");
  Serial.println(tiempo);
  delay(tiempo*60000);
  if(cantidad > 1){
    startInterval(tiempo,cantidad-1);
  }else{
    return;
  }
}


long microsecondsToMillimeters(long microseconds)
{return microseconds / 2.9 / 2;}
