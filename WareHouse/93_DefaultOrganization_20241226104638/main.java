/**
 * This is the main class that serves as the entry point for the web application.
 */
import com.sun.net.httpserver.HttpServer;
import java.net.InetSocketAddress;
public class Main {
    public static void main(String[] args) throws Exception {
        // Create an HTTP server on port 8080
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        // Set up the request handler
        server.createContext("/", new RequestHandler());
        // Start the server
        server.start();
    }
}