import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

class Bracket {
    Bracket(char type, int position) {
        this.type = type;
        this.position = position;
    }

    boolean Match(char c) {
        if (this.type == '[' && c == ']')
            return true;
        if (this.type == '{' && c == '}')
            return true;
        if (this.type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
}

class check_brackets {
    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();
        Bracket top = null;

        Boolean result = null;

        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        for (int position = 0; position < text.length(); ++position) {
            char next = text.charAt(position);

            if (next == '(' || next == '[' || next == '{') {
                // Process opening bracket, write your code here
                Bracket bracket = new Bracket(next, position);
                //bracket.type = next;
                //System.out.println("pushing to stack.." + bracket.type);
                opening_brackets_stack.push(bracket);
            }

            if (next == ')' || next == ']' || next == '}') {
                // Process closing bracket, write your code here

                if (opening_brackets_stack.empty()){
                    //System.out.println("stack empty!");
                    result = false;
                    System.out.println(position + 1);
                    return;
                }

                top = opening_brackets_stack.pop();

                if ((top.type == '(' && next != ')') || (top.type == '[' && next != ']') || (top.type == '{' && next != '}')){
                    result = false;
                    System.out.println(position + 1);
                    return;
                }
            }
        }
        if(opening_brackets_stack.empty()){
            //System.out.println("Success");
            //break;
            result = true;
        }else{
            result = false;
            top = opening_brackets_stack.pop();
        }

        // Printing answer, write your code here
        if (result.equals(true)){
            System.out.println("Success");
        }
        else{
            System.out.println(top.position + 1);
        }
    }
}
