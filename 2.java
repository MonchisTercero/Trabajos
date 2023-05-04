import javax.swing.*;

public class SumaMatrices
{
    private int A[][];
    private int B[][];
    private int c[][];
    private String salida = "\t SUMA DE DOS MATRICES A(nXm) y B(sXt) \n\n";
    JTextArea print;

    public void llenarMatriz()
    {
    	//Defino los tamaños de las matrices en  forma aleatoria.
        A = new int[(int) (10.0 * Math.random()) + 1][(int) (10.0 * Math.random()) + 1];
        B = new int[(int) (10.0 * Math.random()) + 1][(int) (10.0 * Math.random()) + 1];
        //Lleno las matrices anteriores de forma aleatoria.
        for(int f = 0; f < A.length; f++)
        {
            for(int i = 0; i < A[f].length; i++)
            {
                A[f][i] = (int) (10.0 * Math.random())+ 1;
            }
        }

        for(int f = 0; f < B.length; f++)
        {
            for(int i = 0; i < B[f].length; i++)
            {
                B[f][i] = (int) (10.0 * Math.random())+ 1;
            }
        }
    }

    public void sumaMatriz()
    {
        int filasC = 0, ColumnasC = 0;

    	//comparo los tamaños de la matriz A y B y defino el nuevo tamaño de la matriz C.
        if(A.length > B.length)
        {
            filasC = A.length;
        }
        else
        {
            filasC = B.length;
        }
        if(A[0].length > B[0].length )
        {
            ColumnasC = A[0].length;
        }
        else
        {
            ColumnasC = B[0].length;
        }

        c = new int[filasC][ColumnasC];
        //Fin de la comparación de las matrices y asignación del nuevo tamaño de la matriz C.
        
        
        for(int i = 0; i < c.length; i++)
        {
            for(int f = 0; f < c[i].length; f++)
            {
            	//Primera combinación. A > B Y A.i < B.i.
                if(A.length -1 >= B.length - 1 && A[0].length - 1 <= B[0].length - 1)
                {
                	System.out.println("Primera conbinacion");
                	if(i <= B.length - 1 && f <= A[0].length - 1)
                	{
                		c[i][f] = A[i][f] + B[i][f];
                	}
                	else if(i <= B.length - 1 && f >= A[0].length - 1)
                	{
                		c[i][f] = B[i][f];
               		}
                	else if(i >= A.length - 1 && f <= A[0].length - 1)
                	{
                		c[i][f] = A[i][f];
                	}
                	
                }
            	//Segunda  combinación. A > B Y A,i > B,i
                if(A.length -1 >= B.length - 1 && A[0].length - 1 >= B[0].length - 1)
                {
                	System.out.println("Segunda conbinacion");
                	if(i <= B.length - 1 && f <= B[0].length - 1)
                	{
                		c[i][f] = A[i][f] + B[i][f];
                	}
                	else if(i <= B.length - 1 && f >= B[0].length - 1)
                	{
                		c[i][f] = A[i][f];
               		}
                	else if(i > B.length - 1 && f <= A[0].length - 1)
                	{
                		c[i][f] = A[i][f];
                	}
                	
                }
            	//Tercera  combinación. A < B Y A,i < B,i
                if(A.length -1 <= B.length - 1 && A[0].length - 1 <= B[0].length - 1)
                {
                	System.out.println("Tercera conbinacion");
                	if(i <= A.length - 1 && f <= A[i].length - 1)
                	{
                		c[i][f] = A[i][f] + B[i][f];
                	}
                	else if(i <= B.length - 1 && f <= A[0].length - 1)
                	{
                		c[i][f] = B[i][f];
               		}
                	else if(i <= B.length - 1 && f >= A[0].length - 1)
                	{
                		c[i][f] = B[i][f];
                	}
                	
                }
            	//Cuarta  combinación. A < B Y A,i > B,i
                if(A.length -1 <= B.length - 1 && A[0].length - 1 >= B[0].length - 1)
                {
                	System.out.println("Cuarta conbinacion");
                	if(i <= A.length - 1 && f <= B[0].length - 1)
                	{
                		c[i][f] = A[i][f] + B[i][f];
                	}
                	else if(i <= A.length - 1 && f <= A[0].length - 1)
                	{
                		c[i][f] = A[i][f];
               		}
                	else if(i <= B.length - 1 && f <= B[0].length - 1)
                	{
                		c[i][f] = B[i][f];
                	}
                }
            }    
       }
   }

    

    public void pantalla()
    {
        print = new JTextArea();

        salida += "\t\n MATRIZ  A" + "(" + A.length +" X " + A[0].length +  ") \n";
        for(int f = 0; f < A.length; f++)
        {
            for(int i = 0; i < A[f].length; i++)
            {
                salida += A[f][i] + "\t";
            }
            salida += "\n";
        }

        salida += "\t\n MATRIZ  B" + "(" + B.length +" X " + B[0].length +  ") \n\n";
        for(int f = 0; f < B.length; f++)
        {
            for(int i = 0; i < B[f].length; i++)
            {
                salida += B[f][i] + "\t";
            }
            salida += "\n";
        }
        
        salida += "\n\tSUMATORIA DE LAS DOS MATRICES ES: \n\n";
        salida += "\t MATRIZ  C" + "(" + c.length +" X " + c[0].length +  ") \n\n";
        for(int f = 0; f < c.length; f++)
        {
            for(int i = 0; i < c[f].length; i++)
            {
                salida += c[f][i] + "\t";
            }
            salida += "\n";
        }

        print.setText(salida);
        JOptionPane.showMessageDialog(null, print,
				"SUMATORIA DE DOS MATRICES",
				JOptionPane.INFORMATION_MESSAGE);

    }

        public static void main(String[] args)
        {
            SumaMatrices matriz = new SumaMatrices();
            matriz.llenarMatriz();
            matriz.sumaMatriz();
            matriz.pantalla();
        }

}