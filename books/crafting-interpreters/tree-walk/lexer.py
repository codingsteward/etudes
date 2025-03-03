# Write a lexer in Python that hopefully interprets Scheme/Lisp lol
import sys



class LispyLexer:
    """Can either read file and execute it or interactively and execute one code at a time (REPL)"""
    had_error = False

    def __init__(self):
        pass
    
    def run_file(self, path:str) -> None:
        """Reads a file and executes it"""
        print(path)
        with open(path) as reader:
            source = reader.read()
            print(source)
            self.run(source)
        if LispyLexer.had_error:
            sys.exit()
        pass

    def run_prompt(self) -> None:
        """Start interactive prompt: read, eval, print, loop"""
        while True:
            # read, eval, print, loop
            pass
        LispyLexer.had_error = False

    def run(self, source:str) -> None:
        """scan source and group it into tokens"""
        return
        scanner = LispyScanner(source)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)

    @classmethod
    def error(cls, line: int, message: str) -> None:
        report(line, "", message)
    
    @classmethod
    def report(cls, line: int, where: str, message: str) -> None:
        print("[line " + line + "] Error" + where + ": " + message)
        cls.had_error = True




if __name__ == "__main__":
    lexer = LispyLexer()
    if len(sys.argv) <= 1: # no arguments
        lexer.run_prompt()
    else:
        filename = sys.argv[1]
        lexer.run_file(filename)

