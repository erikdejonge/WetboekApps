//
//  VerzekeringsrechtAppDelegate.m
//  Verzekeringsrecht
//
//  Created by rabshakeh on 3/1/10 - 4:25 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import "VerzekeringsrechtAppDelegate.h"
#import "TableViewFromDatabaseViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "WetboekSearchViewController.h"


@implementation VerzekeringsrechtAppDelegate

@synthesize window;
@synthesize viewController;

-(void) applicationDidFinishLaunching: (UIApplication *) application
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;
  
  tableViewFromDatabaseController.table_name = @"wetboekhoofdstuk" ;
  tableViewFromDatabaseController.next_table = @"wetboek" ;
  tableViewFromDatabaseController.title      = @"Verzekerings - Apr. 2011" ;
  [tableViewFromDatabaseController reload] ;
  WetboekSearchViewController *wsvc = [[WetboekSearchViewController alloc] init] ;
  if (NO) {
    navigationController = [[UINavigationController alloc] initWithRootViewController:wsvc] ;
  }
  else{
    navigationController = [[UINavigationController alloc] initWithRootViewController:tableViewFromDatabaseController] ;
  }
  [tableViewFromDatabaseController release] ;
  navigationController.navigationBar.tintColor = [UIColor colorWithRed:0.156862745098 green:0.341176470588 blue:0.545098039216 alpha:0] ;
  
  [window addSubview:[navigationController view]] ;
  
  [window makeKeyAndVisible] ;
  [wsvc release] ;
}


-(void) dealloc
{
  [navigationController release] ;
  [viewController release] ;
  [window release] ;
  [super dealloc] ;
}


@end
