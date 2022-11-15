// Se definen las variables para los pines
// Para el sensor ultrasonico
const int Echo = 2;
const int Trigger = 3;

// Para el driver del motor
const int Enable = 4;
const int DirA = 5;
const int DirB = 6;

// Otras variables
bool cond;
int vel = 360; // Velocidad del motor
int startVar = 0;
int intervalos = 0; // Almacena la cantidad de intervalos ingresados
int tiempo; // Variable temporal para almacenar en Tiempos[]
int cantidad; // Variable temporal para almacenar en Cantidades[]
int Tiempos[16]; // Almacena los tiempos ingresados por el usuario
int Cantidades[16]; // Almacena las cantidades ingresadas por el usuario
int det;
long distancia; // Distancia ultrasonico en centimetros
long tiempo_sensor; // Timepo que demora en llegar el eco en el sensor

void setup() {
  // Configuracion puerto serial
  Serial.begin(9600); // Se inicia la comunicacion

  // Definicion de entradas y salidas
  pinMode(Echo, INPUT);
  pinMode(Trigger, OUTPUT);
  pinMode(Enable, OUTPUT);
  pinMode(DirA, OUTPUT);
  pinMode(DirB, OUTPUT);

  // Se inicializan las salidas
  digitalWrite(Trigger, LOW);
  digitalWrite(Enable, HIGH);
  digitalWrite(DirA, HIGH);
  digitalWrite(DirB, HIGH);
}

void loop() {

}

/* Handler de la interrupcion del puerto serial
 * el cual recibe la cantidad de intervalos y
 * llama a la funcion getIntervalos            */
void serialEvent(){
  while (Serial.available()){
    intervalos = Serial.parseInt();
    if (intervalos != 0){
      getIntervals(intervalos);
    }
  }
}

/* Funcion encargada de recibir los datos de tiempo 
 *  y cantidad para ejecutar la logica del motor y  
 *  el sensor                                      */
void getIntervals(int intervalos){
  // Se envian los datos a la interfaz
  Serial.println(intervalos);
  
  // Se reciben los datos de tiemnpos y cantidades
  for(int i = 0; i <= intervalos - 1; i++){
    tiempo = Serial.parseInt();
    Tiempos[i] = tiempo;
    Serial.println(Tiempos[i]);
    cantidad = Serial.parseInt();
    Cantidades[i] = cantidad;
    Serial.println(Cantidades[i]);
  }

  // Se inicia la secuencia del motor y sensor
  for(int i = 0; i <= intervalos - 1; i++){
    startApp(Tiempos[i], Cantidades[i]);
  }
}

/* Funcion encargada de realizar la
 * secuecia en el motor y en el sensor */
void startApp(int tiempo, int cantidad){
  digitalWrite(DirA, LOW);
  distancia = 50;
  while(distancia < 400){
    digitalWrite(Trigger, HIGH);
    delayMicroseconds(10);                     // Enviamos un pulso de 10us
    digitalWrite(Trigger, LOW);
    tiempo_sensor = pulseIn(Echo, HIGH);       // Obtenemos el ancho del pulso
    distancia = microsecondsToMillimeters(tiempo_sensor);  // Escalamos el tiempo a una distancia en mm
  }
  while(distancia >= 145 || distancia <= 100){
    digitalWrite(Trigger, HIGH);
    delayMicroseconds(10);                     // Enviamos un pulso de 10us
    digitalWrite(Trigger, LOW);
    tiempo_sensor = pulseIn(Echo, HIGH);       // Obtenemos el ancho del pulso
    distancia = microsecondsToMillimeters(tiempo_sensor);  // Escalamos el tiempo a una distancia en mm
  }
  Serial.println("9");
  digitalWrite(DirA, HIGH);
  digitalWrite(DirB, LOW);
  delay(100);
  digitalWrite(DirB, HIGH);
  delay(tiempo*60000);
  if(cantidad > 1){
    startApp(tiempo, cantidad-1);
  }
  else{
    return;
  }
}

long microsecondsToMillimeters(long microseconds)
{
  long d = 0;
  d = microseconds / 2.9 / 2;
  return d;
  }
