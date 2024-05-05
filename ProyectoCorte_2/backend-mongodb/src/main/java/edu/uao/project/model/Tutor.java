package edu.uao.project.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;

@Data
@Document(collection ="Tutors")
public class Tutor {
	@Id
	private String id;
	private String nombre;
	private Integer codigo;
	private Integer semestre;
	private String carrera;

}
