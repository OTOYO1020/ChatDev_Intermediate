'''
Main entry point for the graph simulation application.
'''
def main():
    import sys
    from app import App
    input_data = sys.stdin.read().strip().splitlines()
    app = App(input_data)
    app.run_simulation()
if __name__ == "__main__":
    main()