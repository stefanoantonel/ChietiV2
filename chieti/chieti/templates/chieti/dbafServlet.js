package ar.edu.ucc.bda.web.servlets;

import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import ar.edu.ucc.bda.web.utiles.Constantes;


@WebServlet("/getClientesJSON")
public class GetClientesJSON extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
  
    public GetClientesJSON() {
        super();
        
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		Object term=request.getParameter("term");
		JSONArray clientes=new JSONArray(); //cremoa un objeto json array
		
		
		try {
			Connection cn=(Connection)getServletContext().getAttribute(Constantes.NOMBRE_CONEXION);
			Statement select=cn.createStatement(); //creo el statement. 
			ResultSet rs= select.executeQuery("select* from clientes where Cliente like '%"+term+"%'"); //ejecuto y lo guardo si o si en un 
			//result set que es especial para gusardar el resultado 
			
			
			while(rs.next()){
				JSONObject cliente=new JSONObject();
				cliente.put("id", rs.getString("idCliente"));	//agrego al objeto los atributos
				cliente.put("label", rs.getString("cliente"));
				cliente.put("value", rs.getString("cliente"));
				clientes.put(cliente); //lo pongo en el array
				
			}
		} catch ( SQLException | JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		response.setContentType("application/json");
		response.getWriter().println(clientes.toString());
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
	}

}
