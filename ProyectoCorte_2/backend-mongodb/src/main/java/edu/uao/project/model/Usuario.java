package edu.uao.project.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;

@Data
@Document(collection = "Users")
public class Usuario {
	@Id
	private String id;
	private String document;
	private String name;

}
