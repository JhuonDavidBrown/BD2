package edu.uao.project.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;

@Data
@Document(collection = "TutorsCourses")
public class TutorCurso {
	@Id
	private String id;
	private String nombre;
	private Integer cursos[];
	
}
