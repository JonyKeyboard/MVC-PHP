<?php

namespace App\Controller\Pages;

use \App\Utils\View;

class Home {

    /**
     * Retorna o conteúdo (view) da home
     * @return string
     */
    public static function getHome() {
        return View::render("pages/home", [
            'name' => "MVC - COURSE",
            'description' => "Course: https://www.youtube.com",
            'site' => "Youtube"
        ]);
    }

}