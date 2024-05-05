package edu.uao.project.model;


import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import lombok.Data;

@Data//para getters y setters
@Document(collection = "CoursesRating")//definiendo como documento(entidad)
public class CursoNota {
	@Id
	private String id;
	private String nombre;
    private Double ratings[];
}
