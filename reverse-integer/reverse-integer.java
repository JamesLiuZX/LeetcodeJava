class Solution { //create a stack for integers using modulo 
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            //Main condition that catches overflow/underflow for rev >2147483650 and <-2147483650. (-2147483648 <= rev <= 2147483647)
            if (rev > Integer.MAX_VALUE/10 || rev < Integer.MIN_VALUE/10){                          
                return 0;
            }
            //Secondary condition that catches -2147483650 < rev < -2147483648 and 2147483647 < rev < 2147483650.
            if (rev == Integer.MIN_VALUE/10 && pop > 7 || rev == Integer.MIN_VALUE/10 && pop <-8){
                return 0;
            }
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
