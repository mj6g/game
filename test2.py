import time
import threading

KERET = "--------------------------------------------------------------------------"
URES  = "{                                                                        }"
TALAJ = "{########################################################################}"

# 4 fázisú lélegző álló animáció
ALLO_FAZISOK = [
    [
        KERET,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]            *                                         }",
        "{            {OOO}            I                                          }",
        "{             (O)            I                                           }",
        "{          @GGOOOGG@        I                                            }",
        "{         H {ĐĐĐĐĐ} H      I                                             }",
        "{        H  [&&@&&]  H    I                                              }",
        "{        HH [&&&&&]   GG****                                             }",
        "{          @ &&&&&     GI                                                }",
        "{            @&@&@     I                                                 }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    [
        KERET,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]            +                                         }",
        "{            {OOO}            I                                          }",
        "{             (O)            I                                           }",
        "{          @GGOOOGG@        I                                            }",
        "{         H {ĐĐĐĐĐ} H      I                                             }",
        "{        H  [&&@&&]  H    I                                              }",
        "{        HH [&&&&&]   GG****                                             }",
        "{          @ &&&&&     GI                                                }",
        "{            @&@&@     I                                                 }",
        "{           {}   {}                                                      }",
        "{          {}     {}                                                     }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    [
        KERET,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]            *                                         }",
        "{            {OOO}            I                                          }",
        "{             (O)            I                                           }",
        "{          @GGOOOGG@        I                                            }",
        "{         H {ĐĐĐĐĐ} H      I                                             }",
        "{        H  [&&&&&]  H    I                                              }",
        "{        HH [&&&&&]   GG****                                             }",
        "{          @ &&&&&     GI                                                }",
        "{            @&@&@     I                                                 }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    [
        KERET,
        URES,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]            .                                         }",
        "{            {OOO}            I                                          }",
        "{             (O)            I                                           }",
        "{          @GGOOOGG@        I                                            }",
        "{         H {ĐĐĐĐĐ} H      I                                             }",
        "{        H  [&&@&&]  H    I                                              }",
        "{        HH [&&&&&]   GG****                                             }",
        "{          @ &&&&&     GI                                                }",
        "{            @&@&@     I                                                 }",
        "{          {}     {}                                                     }",
        "{        ĐĐ         ĐĐ                                                   }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
]

# 12 képkockás kardcsapás animáció (felhúzás -> suhintás -> becsapódás -> visszaállás)
TAMADAS_FAZISOK = [
    # 0. képkocka: Előkészület (enyhe rogyasztás, markolat megfeszítése)
    [
        KERET,
        URES,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]            +                                         }",
        "{            {OOO}            I                                          }",
        "{             (O)            I                                           }",
        "{          @GGOOOGG@        I                                            }",
        "{         H {ĐĐĐĐĐ}  H     I                                             }",
        "{        H  [&&@&&]   H   I                                              }",
        "{        HH [&&&&&]    GG****                                            }",
        "{          @ &&&&&      GI                                               }",
        "{            @&@&@      I                                                }",
        "{          {}     {}                                                     }",
        "{        ĐĐ         ĐĐ                                                   }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 1. képkocka: Kard emelése (vállmagasság)
    [
        KERET,
        URES,
        URES,
        "{                           *                                            }",
        "{             OOO           I                                            }",
        "{           [OPPPO]        I                                             }",
        "{            {OOO}         I                                             }",
        "{             (O)         I                                              }",
        "{          @GGOOOGG@ H    I                                              }",
        "{         H {ĐĐĐĐĐ}   H GG****                                           }",
        "{        H  [&&@&&]     GI                                               }",
        "{        HH [&&&&&]     I                                                }",
        "{          @ &&&&&                                                       }",
        "{            @&@&@                                                       }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 2. képkocka: Kard emelése (majdnem a fej fölött)
    [
        KERET,
        "{                      *                                                 }",
        "{                       I                                                }",
        "{                       I                                                }",
        "{             OOO        I                                               }",
        "{           [OPPPO]      I                                               }",
        "{            {OOO}    H GG***                                            }",
        "{             (O)    H   I                                               }",
        "{          @GGOOOGG@      I                                              }",
        "{         H {ĐĐĐĐĐ}                                                      }",
        "{        H  [&&@&&]                                                      }",
        "{        HH [&&&&&]                                                      }",
        "{          @ &&&&&                                                       }",
        "{            @&@&@                                                       }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 3. képkocka: Magas védőállás kulcskocka (ascii2.txt)
    [
        KERET,
        "{                   I                                                    }",
        "{                    I                                                   }",
        "{                     I                                                  }",
        "{             OOO      *I                                                }",
        "{           [OPPPO]   *HGI                                               }",
        "{            {OOO}    H   I                                              }",
        "{             (O)    H     I                                             }",
        "{          @GGOOOGG@                                                     }",
        "{         H {ĐĐĐĐĐ}                                                      }",
        "{        H  [&&@&&]                                                      }",
        "{        HH [&&&&&]                                                      }",
        "{          @ &&&&&                                                       }",
        "{            @&@&@                                                       }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 4. képkocka: Megfeszített tartás + erővillanás a csúcson
    [
        KERET,
        "{                   +                                                    }",
        "{                   .I                                                   }",
        "{                     I                                                  }",
        "{             OOO      *I                                                }",
        "{           [OPPPO]   *HGI                                               }",
        "{            {OOO}    H   I                                              }",
        "{             (O)    H     I                                             }",
        "{          @GGOOOGG@                                                     }",
        "{         H {ĐĐĐĐĐ}                                                      }",
        "{        H  [&&@&&]                                                      }",
        "{        HH [&&&&&]                                                      }",
        "{          @ &&&&&                                                       }",
        "{            @&@&@                                                       }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 5. képkocka: Suhintás indítása (felső ív + mozgáscsík)
    [
        KERET,
        "{                    . .                                                 }",
        "{                       . .       *                                      }",
        "{                               II                                       }",
        "{             OOO             II                                         }",
        "{           [OPPPO]         II                                           }",
        "{            {OOO}        II                                             }",
        "{             (O)    HHGG***                                             }",
        "{          @GGOOOGG@    I                                                }",
        "{         H {ĐĐĐĐĐ}                                                      }",
        "{        H  [&&@&&]                                                      }",
        "{        HH [&&&&&]                                                      }",
        "{          @ &&&&&                                                       }",
        "{            @&@&@                                                       }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 6. képkocka: Gyors vágóív (középső ív)
    [
        KERET,
        URES,
        URES,
        "{                              . . .                                     }",
        "{             OOO                 . .  *                                 }",
        "{           [OPPPO]                 :II                                  }",
        "{            {OOO}                 II                                    }",
        "{             (O)               II                                       }",
        "{          @GGOOOGG@HH        II                                         }",
        "{         H {ĐĐĐĐĐ}    HHHGGG****                                        }",
        "{        H  [&&@&&]        II                                            }",
        "{        HH [&&&&&]                                                      }",
        "{          @ &&&&&                                                       }",
        "{            @&@&@                                                       }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 7. képkocka: Teljes előrecsapás kulcskocka (asdcii3.txt)
    [
        KERET,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]                   *                                  }",
        "{            {OOO}                  II                                   }",
        "{             (O)                 II                                     }",
        "{          @GGOOOGG@HH          II                                       }",
        "{         H {ĐĐĐĐĐ}   HHH     II                                         }",
        "{        H  [&&@&&]      HH ****                                         }",
        "{        HH [&&&&&]        GGG                                           }",
        "{          @ &&&&&         II                                            }",
        "{            @&@&@        I                                              }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 8. képkocka: Becsapódási villanás (hit-stop energiaív)
    [
        KERET,
        URES,
        URES,
        URES,
        "{             OOO                       +                                }",
        "{           [OPPPO]                   * * )                              }",
        "{            {OOO}                  II   )                               }",
        "{             (O)                 II    *                                }",
        "{          @GGOOOGG@HH          II                                       }",
        "{         H {ĐĐĐĐĐ}   HHH     II                                         }",
        "{        H  [&&@&&]      HH ****                                         }",
        "{        HH [&&&&&]        GGG                                           }",
        "{          @ &&&&&         II                                            }",
        "{            @&@&@        I                                              }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 9. képkocka: Utórezgés (lendületi rogyasztás)
    [
        KERET,
        URES,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]                    +  .                              }",
        "{            {OOO}                   II                                  }",
        "{             (O)                  II                                    }",
        "{          @GGOOOGG@HH           II                                      }",
        "{         H {ĐĐĐĐĐ}    HHH     II                                        }",
        "{        H  [&&@&&]       HH ****                                        }",
        "{        HH [&&&&&]         GGG                                          }",
        "{          @ &&&&&           II                                          }",
        "{            @&@&@          I                                            }",
        "{          {}     {}                                                     }",
        "{        ĐĐ         ĐĐ                                                   }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 10. képkocka: Visszahúzás 1. fázis
    [
        KERET,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]                                                      }",
        "{            {OOO}                 *                                     }",
        "{             (O)                 I                                      }",
        "{          @GGOOOGG@            I                                        }",
        "{         H {ĐĐĐĐĐ}  H        I                                          }",
        "{        H  [&&@&&]   HH    I                                            }",
        "{        HH [&&&&&]      GG****                                          }",
        "{          @ &&&&&        GI                                             }",
        "{            @&@&@        I                                              }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
    # 11. képkocka: Visszahúzás 2. fázis (visszatérés alapállásba)
    [
        KERET,
        URES,
        URES,
        URES,
        "{             OOO                                                        }",
        "{           [OPPPO]               *                                      }",
        "{            {OOO}               I                                       }",
        "{             (O)              I                                         }",
        "{          @GGOOOGG@          I                                          }",
        "{         H {ĐĐĐĐĐ}  H       I                                           }",
        "{        H  [&&@&&]   H    I                                             }",
        "{        HH [&&&&&]     GG****                                           }",
        "{          @ &&&&&       GI                                              }",
        "{            @&@&@       I                                               }",
        "{           {}   {}                                                      }",
        "{         ĐĐ       ĐĐ                                                    }",
        "{       {}           {}                                                  }",
        "{      {}             {}                                                 }",
        "{    ###               ###                                               }",
        TALAJ,
        KERET,
    ],
]

eltolas_x = 0
allapot = "idle"       # "idle" vagy "attack"
aktualis_frame = 0
fut_a_jatek = True
allapot_zar = threading.Lock()


def sor_eltolasa(sor, dx):
    """A belső 72 karakter eltolása vízszintesen."""
    belso = sor[1:-1]
    if dx > 0:
        uj_belso = (" " * dx) + belso[:-dx]
    elif dx < 0:
        uj_belso = belso[-dx:] + (" " * (-dx))
    else:
        uj_belso = belso
    return "{" + uj_belso + "}"


def animacio_rajzolo():
    global aktualis_frame, allapot
    while fut_a_jatek:
        with allapot_zar:
            if allapot == "attack":
                kepkocka = TAMADAS_FAZISOK[aktualis_frame]
                varakozas = 0.13  # Gyors, feszes kardcsapás tempó

                aktualis_frame += 1
                if aktualis_frame >= len(TAMADAS_FAZISOK):
                    allapot = "idle"
                    aktualis_frame = 0
            else:
                kepkocka = ALLO_FAZISOK[aktualis_frame]
                varakozas = 0.28  # Nyugodt lélegző tempó
                aktualis_frame = (aktualis_frame + 1) % len(ALLO_FAZISOK)

            dx = eltolas_x

        kirajzolt_sorok = []
        for idx, sor in enumerate(kepkocka):
            # A teljes belső teret (1..18) eltoljuk, hogy a magasra emelt kard is kövesse a karaktert
            if 1 <= idx <= 18:
                kirajzolt_sorok.append(sor_eltolasa(sor, dx))
            else:
                kirajzolt_sorok.append(sor)

        try:
            with open("kepernyo.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(kirajzolt_sorok))
        except PermissionError:
            pass

        time.sleep(varakozas)


szal = threading.Thread(target=animacio_rajzolo, daemon=True)
szal.start()

print("Jatek elindult! Nyisd meg a 'kepernyo.txt' fajlt.")
print("Iranyitas: f (kardcsapas), a (balra), d (jobbra), q (kilepes)")

while fut_a_jatek:
    parancs = input("Parancs > ").strip().lower()
    with allapot_zar:
        if parancs == "f":
            allapot = "attack"
            aktualis_frame = 0
        elif parancs == "a" and eltolas_x > -3:
            eltolas_x -= 2
        elif parancs == "d" and eltolas_x < 26:
            eltolas_x += 2
        elif parancs == "q":
            fut_a_jatek = False
            print("Kilepes...")