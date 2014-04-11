import java.lang.Math;
import java.util.ArrayList;
import java.util.List;

public class Problem47 {

    public static List<Integer> primeSieve(int n) {
        boolean[] sieve = new boolean[n+1];
        for (int i = 2; i <= n; i++) {
            sieve[i] = true;
        }

        for (int i = 2; i <= Math.sqrt(n); i++){
            if (sieve[i]) {
                for (int j = i*2; j <= n; j *= i) {
                    sieve[j] = false;
                }
            }
        }

        ArrayList<Integer> rtn = new ArrayList<Integer>();
        for (int i = 2; i <= n; i++){
            if (sieve[i]){
                rtn.add(i);
            }
        }

        return rtn;
    }

    public static void main(String[] args){
        System.out.printf(Problem47.primeSieve(100).toString());
    }
}