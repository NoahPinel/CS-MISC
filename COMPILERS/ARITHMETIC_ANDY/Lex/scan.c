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
    TOKEN_WTF,
} TokenType;

typedef struct 
{
    TokenType type;
    char lexeme[MAX_TOKEN_SIZE];
    int line_number;
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

char peek_char(FILE *file)
{
    char c = fgetc(file);

    if (c == EOF)
    {
        ungetc(c, file);
        return '\0';
    }

    ungetc(c, file);
    return c;
}

Token get_token(FILE *file, int *line_number)
{
    char c;
    Token token;
    token.type = TOKEN_WTF;
    memset(token.lexeme, 0, MAX_TOKEN_SIZE);
    token.line_number = *line_number;

    do
    {
        c = get_char(file);
        if (c == '\n') 
        {
            (*line_number)++;
            token.line_number = *line_number;
        }
    } while (isspace(c) && c != '\0');

    if (c == '\0')
    {
        token.type = '\0'; // Indicates end of file
        return token;
    }

    if (c == '+')
    {
        token.type = TOKEN_ADD; 
        strncpy(token.lexeme, "+", MAX_TOKEN_SIZE);
    }

    else if (c == '-')
    {
        token.type = TOKEN_SUB; 
        strncpy(token.lexeme, "-", MAX_TOKEN_SIZE);
    }
    
	else if (c == '/')
    {
        token.type = TOKEN_DIV; 
        strncpy(token.lexeme, "/", MAX_TOKEN_SIZE);
    }
    
	else if (c == '*')
    {
        token.type = TOKEN_MULT; 
        strncpy(token.lexeme, "*", MAX_TOKEN_SIZE);
    }
    
	else if (c == '(')
    {
        token.type = TOKEN_LPAR; 
        strncpy(token.lexeme, "(", MAX_TOKEN_SIZE);
    }
    
	else if (c == ')')
    {
        token.type = TOKEN_RPAR; 
        strncpy(token.lexeme, ")", MAX_TOKEN_SIZE);
    }
    
	else if (isdigit(c))
    {
        int i = 0;
        token.lexeme[i++] = c;

        while (isdigit(peek_char(file)))
        {
            c = get_char(file);
            if (c == '\0') break;
            token.lexeme[i++] = c;
        }

        token.lexeme[i] = '\0';
        token.type = TOKEN_INT;
    }
    
	else
    {
        token.type = TOKEN_WTF;
    }

    return token;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: %s <file>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file: %s\n", argv[1]);
        return 1;
    }

    int line_number = 1;
    Token token;
    while (1)
    {
        token = get_token(file, &line_number);
        if (token.type == '\0')
        {
            break;
        }

        if (token.type != TOKEN_WTF)
        {
            printf("%d: Type <%d> %s\n", token.line_number, token.type, token.lexeme);
        }
        
		else
        {
            printf("[ERROR] %d: Type <%d>\n", token.line_number, token.type);
        }
    }

    fclose(file);
    return 0;
}
