import java.util.Objects;


public class Weather {
    /* 
     {
        "city": "Baku",
        "temperature": "23.45"    
     }
    */

    public String city;
    public Double temperature;

    public Weather() {}

    public Weather (String city, Double temperature) {
        this.city = city;
        this.temperature = temperature;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Weather{");
        sb.append("city=").append(city).append('\'');
        sb.append("temperature=").append(String.valueOf(temperature)).append('\'');
        return sb.toString();
    }

    public int hashCode () {
        return Objects.hash(super.hashCode(), city, temperature);
    }

}
