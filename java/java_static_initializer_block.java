

//Write your code here
private static boolean flag = true;
private static int B;
private static int H;
static {
    try{
        BufferedReader input = new BufferedReader(new InputStreamReader  (System.in));
        B = Integer.parseInt(input.readLine());
        H = Integer.parseInt(input.readLine());
        if(B < 0 || H < 0){
            System.out.println("java.lang.Exception: Breadth and height must be positive"); //smirk
            System.exit(0);
        }
        input.close();
    } catch(IOException e){
        e.printStackTrace();
    }
}

