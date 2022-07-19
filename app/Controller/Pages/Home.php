<?php

namespace App\Controller\Pages;

use \App\Utils\View;
use \App\Model\Entity\Organization;

class Home extends Page{

    /**
     * Retorna o conteúdo (view) da home
     * @return string
     */
    public static function getHome() {
        //ORGANIZAÇÃO
        $obOganization = new Organization;

        //VIEW DA HOME
        $content =  View::render("pages/home", [
            'name' => $obOganization->name,
            'description' => $obOganization->description,
            'site' => $obOganization->site
        ]);

        //RETURN VIEW DA PAGE
        return parent::getPage("MVC - COURSE - HOME", $content);
    }

}