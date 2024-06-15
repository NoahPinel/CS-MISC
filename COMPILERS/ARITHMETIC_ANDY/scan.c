#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_TOKEN_SIZE 100

typedef enum 
{
    TOKEN_INT = 300,
    TOKEN_ADD,
    TOKEN_MULT,
    TOKEN_SUB,
    TOKEN_DIV,
    TOKEN_LPAR,
    TOKEN_RPAR,
} TokenType;

typedef struct 
{
    TokenType type;
    char lexeme[MAX_TOKEN_SIZE];
} Token;

char get_char(FILE *file)
{
    char c = fgetc(file);
    
    if (c == EOF)
    {
        return '\0';
    }

    return c;
}

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file: %s\n", argv[1]);
        return 1;
    }

    char c = get_char(file);
    int line_number = 1;
    Token token;  // Define a variable of type Token to store current token
    
    while (c != '\0')
    {
		if (!isspace(c))
		{

			if (c == '+')
			{
				token.type = TOKEN_ADD; 
				strncpy(token.lexeme, "+", MAX_TOKEN_SIZE);
				printf("%d: Type <%d> %s\n", line_number, token.type, token.lexeme);
			}
			
			else if (c == '-')
			{
				token.type = TOKEN_SUB; 
				strncpy(token.lexeme, "-", MAX_TOKEN_SIZE);
				printf("%d: Type <%d> %s\n", line_number, token.type, token.lexeme);
			}
			
			else if (c == '/')
			{
				token.type = TOKEN_DIV; 
				strncpy(token.lexeme, "/", MAX_TOKEN_SIZE);
				printf("%d: Type <%d> %s\n", line_number, token.type, token.lexeme);
			}

			else if (c == '*')
			{
				token.type = TOKEN_MULT; 
				strncpy(token.lexeme, "*", MAX_TOKEN_SIZE);
				printf("%d: Type <%d> %s\n", line_number, token.type, token.lexeme);
			}
			
			else if (c == '(')
			{
				token.type = TOKEN_LPAR; 
				strncpy(token.lexeme, "(", MAX_TOKEN_SIZE);
				printf("%d: Type <%d> %s\n", line_number, token.type, token.lexeme);
			}
			
			else if (c == ')')
			{
				token.type = TOKEN_RPAR; 
				strncpy(token.lexeme, ")", MAX_TOKEN_SIZE);
				printf("%d: Type <%d> %s\n", line_number, token.type, token.lexeme);
			}


		}

        else
		{
			if (c == '\n') 
			{
				line_number++;
			}
		}
	
		c = get_char(file);
    }
    
    fclose(file);
    return 0;
}

