import java.util.Calendar;

public class MyCal{
    
    public static String getDay(String d, String m, String y){
        Calendar cal = Calendar.getInstance();
        cal.set(Integer.parseInt(y), Integer.parseInt(m)-1, Integer.parseInt(d));
        int day = cal.get(Calendar.DAY_OF_WEEK);
        if(day == 1) return "SUNDAY";
        if(day == 2) return "MONDAY";
        if(day == 3) return "TUESDAY";
        if(day == 4) return "WEDNESDAY";
        if(day == 5) return "THURSDAY";
        if(day == 6) return "FRIDAY";
        if(day == 7) return "SATURDAY";
        
        return null;
        
    }