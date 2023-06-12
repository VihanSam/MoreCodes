public class car {
    int numWheels = 4;
    int numSeats = 5;
    public String carname ="";
    
    public void Accelerate() {
        System.out.println(carname +" is Accelerating now!");
    }

    public void Brake() {
        System.out.println(carname + " is stopping now!");
    }

    //getters and setters

    public void setName(String inputCarname){

        this.carname = inputCarname;
    }

    public String getName(){

        return this.carname;
    }
    
}
