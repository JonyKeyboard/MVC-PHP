<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\SiteContato;

class ContatoController extends Controller
{
    public function contato(Request $request){

        return view('site.contato');

    }

    public function salvar(Request $request){

        //realizar a validacao dos dados do formulário recebidos no request
        $request->validate([
            'nome' => 'required',
            'telefone' => 'required',
            'email' => 'required',
            'motivo_contato' => 'required',
            'mensagem' => 'required'
        ]);

        //SiteContato::create($request->all());

    }
}
