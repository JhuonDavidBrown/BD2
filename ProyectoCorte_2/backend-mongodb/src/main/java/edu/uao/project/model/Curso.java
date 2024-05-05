package edu.uao.project.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;


@Data//para getters y setters
@Document(collection = "Courses")//definiendo como documento(entidad)

public class Curso {
	
	@Id
	private String id;
    private String name;
    private String category;
    private Integer price;
    private Integer totalHours;
    private String certification;

}
