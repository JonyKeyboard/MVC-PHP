<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\SiteContato;

class ContatoController extends Controller
{
    public function contato(Request $request){
        /*
        print_r($request->all());
        echo $request->input('_token');
        echo $request->input('email');

        $contato = new SiteContato();
        $contato->nome = $request->input('nome');
        $contato->telefone = $request->input('telefone');
        $contato->email = $request->input('email');
        $contato->motivo_contato = $request->input('motivo_contato');
        $contato->mensagem = $request->input('mensagem');

        //print_r($contato->getAttributes());

        $contato->save();
        */

        $contato = new SiteContato();
        $contato->create($request->all());

        //rint_r($contato->getAttributes());

        return view('site.contato');
    }
}
