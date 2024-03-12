import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;


public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        List<Integer> list = new ArrayList<>(5);
        Iterator iterator = list.iterator();
        list.add(1);
        list.add(1);
        list.add(1);
        list.add(1);
        list.add(1);
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
    }
}
