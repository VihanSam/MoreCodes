public class Main {
    public static void main(String[] args) {
        //System.out.println("Hello World");

        //Making Car
        car tesla = new car();
        car acura = new car();

        //Set Tesla Name
        tesla.setName("Tesla");
        tesla.Accelerate();
        tesla.Brake();

        //Set Acura Name
        acura.setName("Acura");
        acura.Accelerate();
        acura.Brake();

      }
}
