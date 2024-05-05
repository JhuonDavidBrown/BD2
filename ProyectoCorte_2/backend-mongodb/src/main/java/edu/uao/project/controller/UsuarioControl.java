package edu.uao.project.controller;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import edu.uao.project.model.Usuario;
import edu.uao.project.service.UsuarioServiceIMPL;
import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/v2")
@RequiredArgsConstructor
public class UsuarioControl {
	
	private final UsuarioServiceIMPL usuarioService;
	
	@PostMapping("/Users")
	public void save(@RequestBody Usuario usuario) {
		usuarioService.save(usuario);
	}
	
	@GetMapping("/Users")
	public List<Usuario> findAll(){
		return usuarioService.findAll();
	}
	
	@GetMapping("/Users/{id}")
	public Usuario findById(@PathVariable String id) {
		return usuarioService.findById(id).get();
	}
	@DeleteMapping("/Users/{id}")
	public void deleteById(@PathVariable String id) {
		usuarioService.deleteById(id);
	}
	@PutMapping("/Users")
	public void update(@RequestBody Usuario usuario) {
		usuarioService.save(usuario);
		
	}
}